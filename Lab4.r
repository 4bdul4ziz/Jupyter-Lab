library(nycflights13)


ans <- flights[origin = "JFK" && month == 6]
ans
head(ans)

sorted <- flights[order("dest", "month")]
sorted
head(sorted)