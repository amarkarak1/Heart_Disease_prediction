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
                sh ' docker build -t HdR:v1 .'
                }
           }
           stage('Run Image') {
                steps {
                sh ' docker run -d -p 8501:8501 --name HdR HdRapp:v1'
                }
           }
           stage('Testing'){
                steps {
                    echo 'Process Complete..'

                    }
           }
    }
}
