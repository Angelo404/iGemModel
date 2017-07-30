
# Script to charachterize the average hamming distance between 13-strings with ACGT
library(data.table)
nucleotides <- c("A","C","T","G")

random_oligonucleotide <- function(n = 13) { # generates a random spacer 
  v <- sample(nucleotides, n, TRUE)
  return (v)
}

gen <- 1000
results <- vector(mode="numeric", length=gen)
for (i in 1:gen ){
  results[i] <- sum(random_oligonucleotide() != random_oligonucleotide() ) # Hdist btween random spacers
}

summary(results)

hist(results)

# Population : Mean of ~9.78 and SD ~1.575309 