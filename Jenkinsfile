pipeline {

agent any

stages {

stage('Clone Repo') {

steps {
git 'https://github.com/avinashkumar-DevOps/hospital-management-devops.git'
}

}

stage('Install Dependencies') {

steps {
sh 'pip install -r requirements.txt'
}

}

stage('Run Tests') {

steps {
sh 'pytest'
}

}

stage('SonarQube Scan') {

steps {
sh 'sonar-scanner'
}

}

stage('Build Docker') {

steps {
sh 'docker build -t hospital-app .'
}

}

stage('Trivy Scan') {

steps {
sh 'trivy image hospital-app'
}

}

stage('Deploy') {

steps {
sh 'docker-compose up -d'
}

}

}
}
