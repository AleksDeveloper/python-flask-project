pipeline{
    agent any
    /* tools{
        
    // }
    // environment{

     }*/
    stages{
        stage('Requisites') {
            steps{
                echo 'Install Python'
                sh 'python3 --version'
                echo 'Now showing the working dir of the cloned repo:\n'
                sh 'pwd'
                sh 'ls -la'
                // echo '\n****Setting up venv****\n'
                // echo 'Installing venv'
                // sh 'pip install '
                echo '\n****Installing Requirements****\n'
                sh 'pip install -r requirements.txt'
            }

        }

        stage('Build') {
            steps {
                echo 'This is the build stage'
                sh 'python3 -m flask run -h 0.0.0.0 -p 8000'
            }
        }

        stage('Deployment') {
            steps {
                echo 'This is the deployment'
            }
        }
    }
}