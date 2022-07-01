pipeline {
        agent any
            stages {
                stage('Clone Repository') {
                /* Cloning the repository to our workspace */
                steps {
                checkout scm
                }
             }
           stage('Build Image') {
                steps {
                sh ' docker build -t diseaseapp:latest .'
                }
           }
           stage('Run Image') {
                steps {
                sh '  docker run -d -p 8501:8501 --name disease diseaseapp:latest'
                }
           }
           stage('Testing'){
                steps {
                    echo 'Process Complete..'

                    }
           }
    }
}
