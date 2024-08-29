pipeline 
{
  agent {
    label "jenkins slave"
  }
  stages {
    stage("Deployment on PROD env"){
      steps {
        sh "docker rm -f webos"
        sh "docker run -dit --name webos -p 80:80 manuupadhya11/pythonflask"        
      }
    }  
  }
}
  
