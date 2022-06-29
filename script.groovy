
def returncreds(){
def map = [:]
map["AWS_ACCOUNT_ID"] = 032956903258
map["AWS_DEFAULT_REGION"]="us-west-2" 
map["IMAGE_REPO_NAME"]="jenkinspipleine"
 map["REPOSITORY_URI"] = "${map["AWS_ACCOUNT_ID"]}.dkr.ecr.${map["AWS_DEFAULT_REGION"]}.amazonaws.com/${map["IMAGE_REPO_NAME"]}"
 

return map
}

return this
