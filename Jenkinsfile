pipeline {
	agent {
		docker {
			image 'node:alpine'
			args '-u 0:0'
		}
	}
	environment {
		SLS_DEBUG=*
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
				sh 'ls -la'
				sh 'npm install -g serverless'
				sh 'serverless plugin install -n serverless-python-requirements'
				sh 'serverless deploy'
			}
		}
	}
}