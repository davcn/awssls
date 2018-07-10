pipeline {
	agent {
	    docker {
	  		image 'base2/sls:latest'
	    }
	}
	stages {

		stage('prepare') {
			steps {
				sh '''
					npm install -g serverless
					npm install serverless-python-requirements
				'''
			}
		}

		stage('Unit test') {
			steps {				
 			    sh 'serverless --help' // to ensure it is installed
			}
		}			
		
		stage('Integration test') {
			steps {
				sh 'serverless deploy --stage dev'
				sh 'serverless invoke --stage dev --function hello'					
			}
		}

		stage('Teardown') {
			steps {				
				echo 'No need for DEV environment now, tear it down'
				sh 'serverless remove --stage dev'	
			}
		}
	 
	 }
	
	
	 environment {
	 		AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
			AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
	 }

}
