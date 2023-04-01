from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from face_as.forms import ProfileForm
from face_as.models import student,Lastface
from django.db.models import Q
import cv2
import numpy as np
import os
import face_recognition
from playsound import playsound
import winsound

last_face = 'no_face'
current_path = os.path.dirname(__file__)
sound_folder = os.path.join(current_path,'sound/')
# face_list_file = os.path.join(current_path, 'face_list.txt')
sound = os.path.join(sound_folder, 'beep.wav')


def home_page(request):
    scanned = Lastface.objects.all().order_by('date').reverse()
    present = student.objects.filter(present=True).order_by('updated').reverse()
    absent = student.objects.filter(present=False).order_by('shift')
    context = {
        'scanned': scanned,
        'present': present,
        'absent': absent,
    }
    return render(request,"index.html", context)

def ajax(request):
    last_face = Lastface.objects.last()
    context = {
        'last_face':last_face
    }
    return render(request, 'ajax.html',context)

def profile(request):
    data=student.objects.all()
    return render(request,"profile.html",{'profile':data})

def scan(request):

    global last_face
    
    known_face_encodings = []
    known_face_names = []


    profiles = student.objects.all()
    for profile in profiles:
        person = profile.image
        image_of_person = face_recognition.load_image_file(f'media/{person}')
        person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
        known_face_encodings.append(person_face_encoding)
        known_face_names.append(f'{person}'[:-4])

    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:

        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    profile = student.objects.get(Q(image__icontains=name))
                    if profile.present == True:
                        pass
                    else:
                        profile.present = True
                        profile.save()

                    if last_face != name:
                        last_face = Lastface(last_face=name)
                        last_face.save()
                        last_face = name
                        winsound.PlaySound(sound, winsound.SND_ASYNC)
                    else:
                        pass

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == 13:
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return redirect("/", last_face)

    


def savestudent(request):
    form = ProfileForm()
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            name= form.cleaned_data['name']
            roll_number= form.cleaned_data['roll_number']
            gender= form.cleaned_data['gender']
            email= form.cleaned_data['email']
            phone= form.cleaned_data['phone']
            branch= form.cleaned_data['branch']
            sem= form.cleaned_data['sem']
            subject = form.cleaned_data['subject']
            image= form.cleaned_data['image']
            shift = form.cleaned_data['shift']
            reg=student(name=name,roll_number=roll_number,gender=gender,email=email,phone=phone,branch=branch,sem=sem,subject=subject,image=image,shift=shift)
            reg.save()
            return redirect("profile")
    else:
        form = ProfileForm()
    context = {'form':form}
    return render(request,'add_stu.html',context) 

              
def edit_profile(request,id):
    pi=student.objects.get(id=id)
    form = ProfileForm(instance=pi)
    if request.method=="POST":
        form = ProfileForm(request.POST,request.POST, instance=pi)
        if form.is_valid():
            form.save()
            redirect("profile")
    else:
        form = ProfileForm()
    context = {'form':form}
    return render(request,'add_stu.html',context)

def delete_profile(request,id):
    profile = student.objects.get(id=id)
    profile.delete()
    return redirect("profile")

def clear_history(request):
    history = LastFace.objects.all()
    history.delete()
    return redirect('index')

def student_total(request):
    dd=student.objects.all()
    return render(request,"student_total.html",{'student_name':dd})

def reset(request):
    profiles = student.objects.all()
    for profile in profiles:
        if profile.present == True:
            profile.present = False
            profile.save()
        else:
            pass
    return redirect('/')