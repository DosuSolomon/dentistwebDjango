from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def service(request):
    return render(request, 'service.html')

def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']
        
        appointment = "Name: "+your_name+"Phone: "+your_phone+"Email: "+your_email+"Address: "+your_address+"Schedule: "+your_schedule+"Day: "+your_date+"Message: "+your_message
        
        send_mail(
            'Appointment Request',  #Subject
            appointment,                        #Message
            'From' + your_email,         #From Email
            ['dosusulaimon.s@gmail.com'],  #To Email
            # fail_silently = False,
        )
        
        
        return render(request, 'appointment.html', {
            'your_name' : your_name,
            'your_phone' : your_phone,
            'your_email' : your_email,
            'your_address' : your_address,
            'your_schedule' : your_schedule,
            'your_date' : your_date,
            'your_message' : your_message
        })
    else:
        return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email =request.POST['message-email']
        message = request.POST['message']
        
        # Send Email
        send_mail(
            'Message from' + message_name,  #Subject
            message,                        #Message
            'From' + message_email,         #From Email
            ['dosusulaimon.s@gmail.com'],  #To Email
            # fail_silently = False,
        )
        
        
        return render(request, 'contact.html', {'message_name':message_name})
    
    else:
        return render(request, 'contact.html')
    
    