from django.conf.urls import url
from aws import GeneratePresignedUrl


awsurls = [
    url('s3presignedurl/(?P<type>([a-z]+))', GeneratePresignedUrl.as_view())
]