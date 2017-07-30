

# Script to prioritize spacers with less off target and more "theoretical" activity
# Activity is calculated based on closeness to heler and by calc Z scores
# Asumes spacer size of 13
library(data.table)

to_z_scores <- function(data){
  pop_sd <- sd(data)*sqrt((length(data)-1)/(length(data)))
  pop_mean <- mean(data)
  return ( (data - pop_mean) / pop_sd )
}



virus <- fread("Desktop/iGEM_modeling/SK1_heller.csv")
virus[,off_t_z := to_z_scores(hits) ] #                   Z score of off traget effects
virus[,activity_z := to_z_scores(reads * (13-dist)) ] #   Heler activity penalized by H distance
virus[,score := activity_z - off_t_z ] #                  good spacers have high act low off_t
write.csv( virus[,.SD[order(-score)]], "sk1_output.csv", row.names = F, quote = F)