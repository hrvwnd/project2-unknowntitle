pipeline{
        agent any

        stages{


                stage('--- update repo and export build number---'){
                    steps{
                            sh ''' export build="${BUILD_NUMBER}"
                            git fetch
                            cd ~/
                            pwd
                            cd recipe-generator
                            git fetch
                            git checkout master
                            git pull origin master
                            '''
                    }

                }
                
                stage('---Prune, build and push images---'){
                    steps{
                            sh '''
                            pwd
                            cd /home/jenkins/recipe-generator
                            git checkout master
                            docker-compose build
                            docker-compose push
                            '''

                    }
                }
                stage('---deploy---'){
                    steps{
                            sh '''ssh -t 5.246.17.1 << EOF
                            cd recipe-generator
			    git pull origin master
                            #docker swarm init
                            ls
                            docker rm -f $(docker ps -qa)
                            docker image prune -af
                            #docker-compose up
                            docker stack deploy --compose-file docker-compose.yaml recipe-generator-app
                            '''
                    }
                }
        }
}