pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Test curl') {
      steps {
        sh 'curl -d "Fac" -X POST http://127.0.0.1:8085/autocomplete'
      }
    }
  }
}