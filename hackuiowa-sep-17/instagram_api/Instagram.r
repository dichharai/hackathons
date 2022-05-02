require(httr)
require(rjson)
require(RCurl)

full_url <- oauth_callback()
full_url <- gsub("(.*localhost:[0-9]{1,5}/).*", x=full_url, replacement="\\1")

invisible(readline(message))

app_name <- "ThinkToStartTest"
client_id <- "CLIENT_ID"
client_secret <- "CLIENT_SECRET"
scope = "public_content"

instagram <- oauth_endpoint(
  authorize = "https://api.instagram.com/oauth/authorize",
  access = "https://api.instagram.com/oauth/access_token")  
myapp <- oauth_app(app_name, client_id, client_secret)

ig_oauth <- oauth2.0_token(instagram, myapp,scope=scope,  type = "application/x-www-form-urlencoded",cache=FALSE)  
tmp <- strsplit(toString(names(ig_oauth$credentials)), '"')
token <- tmp[[1]][30]

user_info <- fromJSON(getURL(paste('https://api.instagram.com/v1/users/self/?access_token=',token,sep="")))

received_profile <- user_info$data$id
media <- fromJSON(getURL(paste('https://api.instagram.com/v1/users/self/media/recent/?access_token=',token,sep="")))


df = data.frame(no = 1:length(media$data))

for(i in 1:length(media$data))
{
  df$posts[i] <-media$data[[i]]$posts$count
  df$followers[i] <- media$data[[i]]$followers$count
  df$date[i] <- toString(as.POSIXct(as.numeric(media$data[[i]]$created_time), origin="1970-01-01"))
}


