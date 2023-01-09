pipeline {
    agent {
        docker {
            image 'node:16'
            args '-p 3000:3000'
        }
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master', url: 'https://github.com/waleed-ahmed15/tcs_node_asgn_devops.git'
            }
        }
        stage('Build application') {
            steps {
                sh "sudo chown -R 115:122 '/.npm'"


                sh 'npm install'
                sh 'npm run build'
            }
        }
    }
}
