pipeline {
    agent any

    stages {
        // stage('Checkout') {
        //     steps {
        //         // Checkout the code from your GitHub repository
        //        git branch: 'main', credentialsId: 'Git-new', url: 'https://github.com/V-vk-404/Task-2.git'
        //     }
        // }
        
        stage('Install Dependencies') {
            steps {
                // Install dependencies using pip
                sh 'pip3 install selenium'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run your unit tests here
                sh 'python3 website_test.py'
            }
        }
    }

    post {
        always {
            // Archive test reports or any other artifacts you want to keep
            archiveArtifacts artifacts: '**/test-reports/*.xml', allowEmptyArchive: true
        }

        success {
            echo 'Unit tests passed! Deploying...'
            // Add deployment steps here, if applicable
        }

        failure {
            echo 'Unit tests failed. Please check and fix the code.'
            // You can send notifications or take other actions on failure
        }
    }
}
