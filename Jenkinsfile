
def gv
def aws_id
pipeline {
    agent any
    stages{
        
         stage('Clone Repository') {
            //cloning repository to our workspace
            steps {
                // Get some code from a GitHub repository
                //git 'https://github.com/amarkarak1/Heart_Disease_prediction.git'
                checkout scm
                 }
            }
       
       
    // Building Docker images
        stage('Building Image') {
          steps{

                 sh ' sudo docker build -t Heart_Disease_predictionapp . '
          }
        }
        
        
         // running  Docker images
        stage('Run Image') {
          steps{

                sh ' sudo docker run -d -p 8501:8501 --name Heart_Disease_prediction Heart_Disease_predictionapp '
          }
        }
        
        
        
}
