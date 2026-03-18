pipeline {

agent any

stages {

stage('Clone Repo') {

steps {
git branch: 'main', url: 'https://github.com/avinashkumar-DevOps/hospital-management-devops.git'
}

}

stage('Install Dependencies') {

steps {
        sh '''
        python3 -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        '''
      }

}

stage('Run Tests') {

steps {
        sh '''
        . venv/bin/activate
        pytest
        '''
      }

}

stage('SonarQube Scan') {

steps {
        sh '''
        /opt/sonar-scanner/bin/sonar-scanner \
        -Dsonar.projectKey=hospital-app \
        -Dsonar.sources=. \
        -Dsonar.host.url=http://localhost:9000 \
        -Dsonar.login=sqa_39c9618985d99d494c7ef78a1d66f4400d3056f1
        '''
    }

}

stage('Build Docker') {

steps {
        sh '''
        docker build -t hospital-app:latest .
        '''
      }

}

stage('Trivy Scan') {

steps {
        sh '''
        trivy image hospital-app:latest
        '''
      }

}

stage('Deploy') {

steps {
        sh '''
        docker compose down || true
        docker rm -f hospital_mysql hospital_app || true
        docker compose up -d --build
        '''
      }

}

}
}
