library(gapminder)
library(dplyr)
library(ggplot2)

data("gapminder")
summary(gapminder)


attach(gapminder)
median(pop)
hist(lifeExp)
hist(log(pop))

boxplot(lifeExp ~ continent)

plot(lifeExp ~ log(gdpPercap))


df1 = gapminder %>%
  select(country, lifeExp) %>%
  filter(country == "South Africa" |
           country == "Ireland") 

t.test(data = df1, lifeExp ~ country)

gapminder %>%
  filter(gdpPercap < 50000) %>%
  ggplot(aes(x=log(gdpPercap), y=lifeExp, col = year, size = pop)) +
  geom_point(alpha=0.75)+
  geom_smooth(method=lm) +
  facet_wrap(~continent)

gapminder %>%
  filter(gdpPercap < 50000) %>%
  ggplot(aes(x=log(gdpPercap), y=lifeExp, col = continent, size = pop)) +
  geom_point(alpha=0.75)+
  geom_smooth(method=lm)

