library(devtools)
library(ggplot2)
library(RColorBrewer)
library(reshape2)
library(plyr)
library(igraph)

library("poweRlaw")

# store the current directory
initial.dir<-getwd()
setwd(initial.dir)

# Calculating Tieness to JS_SR

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_SR_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_SR_unsorted.csv")

# Calculating Tieness to JS_JCSR

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_JCSR_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_JCSR_unsorted.csv")

# Calculating Tieness to T_JS_JCOSR

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_JCOSR_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_JCOSR_unsorted.csv")

# Calculating Tieness to JS_NL

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_NL_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_NL_unsorted.csv")

# Calculating Tieness to JS_PSC

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_PSC_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_PSC_unsorted.csv")

# Calculating Tieness to JS_CT

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_CT_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_JS_CT_unsorted.csv")

# Calculating Tieness to RB_SR

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_SR_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_SR_unsorted.csv")

# Calculating Tieness to RB_JCSR

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_JCSR_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_SR_unsorted.csv")

# Calculating Tieness to RB_JCOSR

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_JCOSR_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_JCSR_unsorted.csv")

# Calculating Tieness to RB_NL

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_NL_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_JCOSR_unsorted.csv")

# Calculating Tieness to RB_PSC

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_PSC_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_PSC_unsorted.csv")

# Calculating Tieness to RB_CT

temp = read.csv("/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_CT_part1.csv", sep=",", encoding="UTF-8")

#Tranform list in data.frame
aux=as.data.frame(temp)

NeighborhoodOverlap = aux$neighborhoodOverlap
Weight = aux$weight
changeNO = aux$changeNO/4

norm_vec <- function(x) (1+((x-min(Weight)*(2-1))/(max(Weight)-min(Weight))))

pair = data.frame(changeNO, Weight<-norm_vec(Weight))

tieness <- ifelse(pair$Weight==1, changeNO/4, (aux$changeNO*pair$Weight)/4)

finalTieness <- data.frame(source<-aux$source, target<-aux$target, tieness)

write.csv(finalTieness, file = "/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/T_RB_CT_unsorted.csv")