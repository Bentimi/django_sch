from django.urls import include, path, re_path
from paymentApp import views as pay

urlpatterns = [
    re_path(r'^payment_details/(?P<user_id>\d+)/(?P<status>\w+)/', pay.paymentDetails, name='payment_details'),
    re_path(r'^payment_confirm/(?P<user_id>\d+)/(?P<status>\w+)/', pay.paymentConfirm, name='payment_confirm'),
    re_path(r'^cancel_payment/(?P<inv_id>\d+)/(?P<status>\w+)/', pay.cancelPayment, name='cancel_payment'),
    re_path(r'^make_payment/(?P<inv_id>\d+)/', pay.makePayment, name='make_payment'),
    re_path(r'^payment_success/(?P<inv_id>\d+)/', pay.paymentSuccess, name='payment_success'),
    re_path(r'^payment_fails/(?P<inv_id>\d+)/', pay.paymentFail, name='payment_fails'),
    # re_path(r'^pdf_download/', pay.DownloadPDF, name='pdf_download'),
    re_path(r'^pdf_view/', pay.viewPDF, name='pdf_view'),
    re_path(r'^pdf/', pay.render_to_pdf, name='pdf'),
]