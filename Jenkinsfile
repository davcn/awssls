pipeline {
	agent {
		dockerfile true
	}
	environment {
		AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
		AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
		AWS_DEFAULT_REGION = 'us-east-1'
	}
	stages {
		stage('Build') {
			steps {
				sh 'echo build'
			}
		}
		stage('Unit Test') {
			steps {
				sh 'pytest functions/test_compute.py'
			}
		}
		stage('Prepare deploy') {
			steps {
				sh 'serverless plugin install -n serverless-python-requirements'
			}
		}
		stage('Deploy') {
			steps {
				sh 'serverless deploy --stage pre-dev'
			}
		}
		stage('Integration Test') {
			steps {
				sh 'echo build'
			}
		}
		stage('Remove Deploy') {
			steps {
				sh 'serverless remove --stage pre-dev'
			}
		}
		stage('Update Deploy') {
			steps {
				sh 'serverless deploy --stage dev'
			}
		}
	}
}