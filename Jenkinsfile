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
                sh 'docker --version'
                echo '\n****Installing Requirements****\n'
                sh 'pip install -r requirements.txt'
            }

        }

        stage('Build') {
            steps {
                echo 'This is the build stage'

                sh '''
                    docker build . -t flasktice-aleks
                    docker tag flasktice-aleks alejandrodjc/flasktice-aleks
                    docker push alejandrodjc/flasktice-aleks
                '''
            }
        }

        stage('Deployment') {
            steps {
                echo 'This is the deployment'
                // sh 'python3 -m flask run -h 0.0.0.0 -p 8000'
            }
        }
    }
}