pipeline {
 agent any
 stages {
  stage('One') {
   steps {
    echo 'Hi, this is yen'
   }
  }
  stage('Two') {
   steps {
    echo 'step 2 '
   }
  }
  stage('Three') {
   parallel {
    stage('Unit Test') {
     steps {
      echo "Running the unit test..."
     }
    }
    stage('Integration test') {

     steps {
      echo "Running the integration test..."
      //sh(returnStdout: true, script: "git clone https://github.com/yennanliu/twitter_real_time_pipeline").trim()

     }
    }
   }
  }
 }
}