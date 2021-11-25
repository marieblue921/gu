pipeline {
    agent any

    stages { 
        stage('Git Clone') {
            steps {  
                script {
                    try{
                        git url: "https://github.com/marieblue921/gu.git", branch: "master" 
                        env.cloneResult=true
                    }catch(error){
                        print(error)
                        env.cloneResult=false
                         currentBuild.result='FAILURE'
                    }
                }
                  
            }
        }
        stage('Docker Build & Push'){
            when{
                expression {
                    return env.cloneResult ==~ /(?i)(Y|YES|T|TRUE|ON|RUN)/
                }
            }
            steps {
                script{
                    try{
                    
                        sh"""
                        cp manifest/Dockerfile ./
                        aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 299522382061.dkr.ecr.ap-northeast-2.amazonaws.com/gu-dev
                        docker build -t ${env.JOB_NAME.toLowerCase()} .
                        docker tag ${env.JOB_NAME.toLowerCase()}:latest 299522382061.dkr.ecr.ap-northeast-2.amazonaws.com/gu-dev:${env.BUILD_NUMBER}
                        docker push 299522382061.dkr.ecr.ap-northeast-2.amazonaws.com/gu-dev:${env.BUILD_NUMBER}
                        docker rmi 299522382061.dkr.ecr.ap-northeast-2.amazonaws.com/gu-dev:${env.BUILD_NUMBER}
                        docker rmi cicd_test
                        """
                         env.dockerBuildResult=true
                    }catch(error){
                        print(error)
                         env.dockerBuildResult=false
                         currentBuild.result='FAILURE'
                    }
                }
            }
        }
        stage('K8S Manifest Update') {
            when{
                expression {
                return env.dockerBuildResult ==~ /(?i)(Y|YES|T|TRUE|ON|RUN)/
                }
            }
            steps {
                script {
                    try{
                        git url: "https://github.com/marieblue921/Infra.git",
                            branch: "master"
                        sh"""
                        git branch -M master
                        sed -i 's/gu-dev:.*\$/gu-dev:${env.BUILD_NUMBER}/g' deployment.yaml
                        git add deployment.yaml
                        git commit -m '[UPDATE] gu-dev image versionig!!'
                        git remote set-url origin git@github.com:marieblue921/Infra.git
                        git push -u origin master
                        """
                        env.tagUpdateResult=true
                    }catch(error){
                        print(error)
                        env.tagUpdateResult=false
                         tagUpdateResult.result='FAILURE'
                    }
                }
                 
            }
            
    }
  }
}
