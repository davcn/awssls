pipeline {
	agent {
		dockerfile true
	}
	environment {
		AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
		AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
	}
	stages {
		stage('Build') {
			steps {
				sh 'echo build'
			}
		}
		stage('Deploy') {
			steps {
				sh 'serverless deploy'
			}
		}
	}
}