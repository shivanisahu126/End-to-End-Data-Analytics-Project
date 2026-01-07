select * from application;

'''Total apps count by category'''
select category, count(app) as Total_apps from application
group by category
order by Total_apps desc;

'''5.0 and above rating app'''
select app, rating from application
where rating = 5.0 ;

'''free and paid apps count'''
select type, count(app) as type_count from application
where type in ('Free','Paid')
group by type;

'''popular apps in game category'''

select app, max(cast (reviews as BIGINT)) as total_reviews from application
where category = 'GAME' 
group by app
order by total_reviews desc limit 10;

'''average rating in each category'''
select app, category, avg(cast(rating as numeric)) as avg_rating from application
group by category, app
having avg(cast(rating as numeric)) > 4.0;

'''teen content rating highest installation app'''
select app, content_rating, installs from application
where content_rating = 'Teen'
group by app, content_rating, installs
order by installs desc limit 10;

'''size is more than 50Mb and rating minimum 4.5'''

select app, size, rating from application
where size >= 50 and rating >= 4.5
order by size desc
limit 10;