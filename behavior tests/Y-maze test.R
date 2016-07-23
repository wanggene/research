library(scales)
library(grDevices)
ent <- 'abcbbccbcbbabaaabc'
## Arm entrance – counted when all four limbs cross into one arm
## Definitions: 
## 1. Total Arm entrance – counted when all four limbs cross into one arm
total.entr <- length(ent)

## 2. # of maximum alternation 

max.alter <- function(x) {length(ent)-2}

## 3. Spontaneous alternation – arms entered that differ from the previous two
spon.alter <- function (x) {
      re <- 0
      i <- length(x)
      for (i in 3:(length(x))) {
            if ( x[i] != x[i-1] & x[i]!= x[i-2] ) {
                  re <- re + 1   
            }
      } 
      return(re)
}
spon.alter(ent)

## 4. Repeated entrance (rep.entr) – an animal crosses into one arm, returns to the center of the Y maze, and then enters the same arm again.
rep.entr <- function (x) {
      re <- 0
      i <- 1
      for (i in 1:(length(x)-1)) {
            if ( x[i] == x[i+1] ) {
                  re <- re + 1   
                  }
            } 
      return(re)
}
rep.entr(ent)
pdf(ymaze.pdf)

## 5. Percent of spontaneous alternation – created as a ratio of number of spontaneous alternation over number of maximum spontaneous alternations multiplied by 100.

pect_spon.alter <- function(x) {
      y<- percent(spon.alter(x)/length(x))
      return(y)
}
pect_spon.alter(ent)



