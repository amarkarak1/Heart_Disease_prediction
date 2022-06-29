
def gv
def aws_id
pipeline {
    
   
    stages {
        stage('init'){
            agent any
            steps{
                script{
                    gv = load "script.groovy"
                    aws_id = gv.returncreds()
                    
                }
            }
        }

       stage('Cleanup Workspace') {
            agent any
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }
        
        stage('Build') {
            agent any
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/amarkarak1/Heart_Disease_prediction.git'

                
                 }
        }
         
        
        
        
  
    // Building Docker images
    stage('Building image') {
        agent any
      steps{
        script {
            dockerImage = sh " docker build -t Heart_Disease_prediction ."
        }
      }
    }
   
  
    

    }
}
