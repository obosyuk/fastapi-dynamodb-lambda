FROM public.ecr.aws/lambda/python:3.12
COPY ./app ./app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
CMD ["app.app.handler"]