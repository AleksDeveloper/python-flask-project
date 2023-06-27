pipeline{
    agent any
    /* tools{
        
    // }
    // environment{

     }*/
    stages{
        stage('Requisites') {
            echo 'Install Python'
            sh 'python3 --version'
            echo 'Now showing the working dir of the cloned repo:\n'
            sh 'pwd'
            sh 'ls -la'
        }

        stage('Test Webhook') {
            steps {
                echo 'Webhook works'
            }
        }

        stage('Build') {
            steps {
                echo 'This is the build stage'
            }
        }

        stage('Deployment') {
            steps {
                echo 'This is the deployment'
            }
        }
    }
}