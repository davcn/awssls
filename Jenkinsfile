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
				sh 'npm install'
			}
		}
		stage('Deploy') {
			steps {
				sh 'npm install -g serverless'
				sh 'serverless plugin install -n serverless-python-requirements'
				sh 'ls -la'
				sh 'ls -la .serverless'
				sh 'serverless deploy'
			}
		}
	}
}