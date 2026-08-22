pipeline {
    agent any

    tools {
        maven 'maven'
    }

    environment {
        AWS_REGION = 'us-east-1'
        ACCOUNT_ID = '702147744538'

        ECR_REPO = 'microservice-demo'
        ECR_URI = "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"
    }

    stages {

        stage('Build') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'mvn clean package'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withSonarQubeEnv('SonarQube') {
                        sh '''
                        mvn sonar:sonar \
                        -Dsonar.projectKey=devops-handson-activities
                        '''
                    }
                }
            }
        }

        stage('Upload Artifact to Nexus') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'mvn deploy'
                }
            }
        }

        stage('Docker Build') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh '''
                    docker build -t microservice-demo:v1 .
                    '''
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh '''
                    trivy image \
                    --severity HIGH,CRITICAL \
                    microservice-demo:v1
                    '''
                }
            }
        }

        stage('ECR Login') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh '''
                    aws ecr get-login-password \
                    --region $AWS_REGION | \
                    docker login \
                    --username AWS \
                    --password-stdin \
                    $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                    '''
                }
            }
        }

        stage('Tag Image') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh '''
                    docker tag microservice-demo:v1 $ECR_URI:${BUILD_NUMBER}
                    docker tag microservice-demo:v1 $ECR_URI:latest
                    '''
                }
            }
        }

        stage('Push Image To ECR') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh '''
                    docker push $ECR_URI:${BUILD_NUMBER}
                    docker push $ECR_URI:latest
                    '''
                }
            }
        }
    }

    post {

        always {
            echo 'Pipeline execution completed.'
        }

        success {
            echo 'Docker image pushed successfully to ECR.'
        }

        unstable {
            echo 'One or more stages failed, but pipeline continued.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
