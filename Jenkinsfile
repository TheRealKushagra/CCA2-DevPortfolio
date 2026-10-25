pipeline {
    agent any

    environment {
        IMAGE_NAME = 'cca2-devportfolio'
        K8S_DEPLOYMENT = 'devportfolio'
        K8S_CONTAINER = 'devportfolio'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/TheRealKushagra/CCA2-DevPortfolio.git'
            }
        }

        stage('Build and Test') {
            steps {
                sh '''
                    python3 --version
                    python3 -m py_compile app.py
                    test -f requirements.txt
                    echo "Python syntax check passed"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DH_USER',
                        passwordVariable: 'DH_TOKEN'
                    )
                ]) {
                    sh '''
                        echo "$DH_TOKEN" | docker login \
                            -u "$DH_USER" --password-stdin

                        docker tag $IMAGE_NAME:$BUILD_NUMBER \
                            "$DH_USER/$IMAGE_NAME:$BUILD_NUMBER"

                        docker tag $IMAGE_NAME:$BUILD_NUMBER \
                            "$DH_USER/$IMAGE_NAME:latest"

                        docker push "$DH_USER/$IMAGE_NAME:$BUILD_NUMBER"
                        docker push "$DH_USER/$IMAGE_NAME:latest"

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DH_USER',
                        passwordVariable: 'DH_TOKEN'
                    )
                ]) {
                    sh '''
                        kubectl apply -f k8s/
                        kubectl set image deployment/$K8S_DEPLOYMENT \
                            $K8S_CONTAINER=$DH_USER/$IMAGE_NAME:$BUILD_NUMBER

                        kubectl rollout status \
                            deployment/$K8S_DEPLOYMENT --timeout=120s
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    kubectl get deployments
                    kubectl get pods
                    kubectl get services
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
