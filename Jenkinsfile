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
                sh ' docker build -t disease:latest .'
                }
           }
           stage('Run Image') {
                steps {
                sh ' docker run -p 8501:8501 disease:latest'
                }
           }
           stage('Testing'){
                steps {
                    echo 'Process Complete..'

                    }
           }
    }
}
