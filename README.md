# Build docker container

     docker build -t labhub_bot .
     docker tag labhub_bot wixxxez/labhub_bot
     docker push  wixxxez/labhub_bot      

## Run container no your local machine 

 Install Ngrok app before 

    ngrock http 80
    docker run -i -t -p 80:8000 labhub_bot

# Deploy bot to GCP Cloud Run

    gcloud services enable containerregistry.googleapis.com
    docker pull wixxxez/labhub_bot
    docker tag wixxxez/labhub_bot  gcr.io/fcitlabhub-api/labhub_bot
    docker push gcr.io/fcitlabhub-api/labhub_bot