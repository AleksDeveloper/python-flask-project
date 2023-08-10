pipeline{
    agent any
    /*tools{

    }*/

    environment{
        scannerHome = tool 'SQS 4.8.0.2856';
     }

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

        stage('Static Code Analysis (SonarQube)') {
            steps {
                echo 'Static Code Analysis'
                withSonarQubeEnv('SonarCloud') {
                    sh '''${scannerHome}/bin/sonar-scanner \
                        -Dsonar.organization=aleksdeveloper \
                        -Dsonar.projectKey=aleksdeveloper_Flasktice \
                        -Dsonar.host.url=https://sonarcloud.io
                    '''
                }
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Unit Tesing'
                sh 'pwd'
                sh 'ls'
                sh 'cd testing'
                script {
                    try {
                        sh '''
                        export PATH="/var/lib/jenkins/.local/bin:$PATH"
                        pytest --cov --html=report.html
                        '''                        
                    }catch(error) {
                        echo error.getMessage()
                    }
                }

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
                script {
                    try {
                        sh '''
                        docker rm -vf $(docker ps -aq)
                        '''
                    }catch(error) {
                        echo error.getMessage()
                    }
                    sh '''
                        env
                        docker run -d --name flaskticeapp -p 8000:8000 --env-file .env alejandrodjc/flasktice-aleks
                        docker ps -a
                    '''
                }
                // sh 'python3 -m flask run -h 0.0.0.0 -p 8000'
            }
        }
    }
}
