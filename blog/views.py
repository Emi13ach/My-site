from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpeg",
        "author": "Emil",
        "date": date(2023, 5, 9),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the view you get when hiking in the mountains. And I wasn't even prepared for what happened whilst I was enjoying the view.",
        "content": """ lorem ipsum dolor sit amet. Fugit nobis pariatur sunt eos quisquam, earum inventore quis ducimus tempora 
                       dolorum cumque aperiam? Fugit tempora facilis. Dolores aliquid eligendi ipsa praesentium quod ab fugiat 
                       minima obcaecati ut. Et quidem hic possimus exercitationem commodi ipsa, id hic quod, dolorum temporibus 
                       
                       dolorem velit cupiditate corporis maxime eum ipsa amet placeat earum, fugit hic adipisci sapiente? Aperiam
                       reiciendis voluptatem mollitia odio quos, voluptate reiciendis voluptatem modi rem corporis in. Iste veritatis 
                       odio vitae animi amet voluptatibus laudantium officia ad deserunt, itaque numquam sint aut accusantium, 
                       exercitationem maiores nihil voluptates, qui facere doloribus harum porro culpa similique repudiandae tenetur 
                       
                       vitae aliquid, fugit error nemo inventore ullam ipsa. Quia rerum repellendus quibusdam quos laborum earum 
                       voluptatem ab, molestiae blanditiis consequatur quis hic dolore at tempora, magni ipsa possimus iure harum, 
                       facilis dolorem iure maiores, eveniet eos porro expedita fuga quae deleniti officiis reprehenderit aspernatur? 
                       Quam labore beatae optio dolore unde nihil a, omnis magnam sequi excepturi atque et repudiandae iure tenetur?"
                       """
    },
        {
        "slug": "green-woods",
        "image": "woods.jpg",
        "author": "Emil",
        "date": date(2023, 4, 9),
        "title": "Green woods",
        "excerpt": "There's nothing like the view you get when hiking in the mountains. And I wasn't even prepared for what happened whilst I was enjoying the view.",
        "content": """ lorem ipsum dolor sit amet. Fugit nobis pariatur sunt eos quisquam, earum inventore quis ducimus tempora 
                       dolorum cumque aperiam? Fugit tempora facilis. Dolores aliquid eligendi ipsa praesentium quod ab fugiat 
                       minima obcaecati ut. Et quidem hic possimus exercitationem commodi ipsa, id hic quod, dolorum temporibus 
                       
                       dolorem velit cupiditate corporis maxime eum ipsa amet placeat earum, fugit hic adipisci sapiente? Aperiam
                       reiciendis voluptatem mollitia odio quos, voluptate reiciendis voluptatem modi rem corporis in. Iste veritatis 
                       odio vitae animi amet voluptatibus laudantium officia ad deserunt, itaque numquam sint aut accusantium, 
                       exercitationem maiores nihil voluptates, qui facere doloribus harum porro culpa similique repudiandae tenetur 
                       
                       vitae aliquid, fugit error nemo inventore ullam ipsa. Quia rerum repellendus quibusdam quos laborum earum 
                       voluptatem ab, molestiae blanditiis consequatur quis hic dolore at tempora, magni ipsa possimus iure harum, 
                       facilis dolorem iure maiores, eveniet eos porro expedita fuga quae deleniti officiis reprehenderit aspernatur? 
                       Quam labore beatae optio dolore unde nihil a, omnis magnam sequi excepturi atque et repudiandae iure tenetur?"
                       """
    },
            {
        "slug": "my-lovly-monutains",
        "image": "mountains-2.jpeg",
        "author": "Emil",
        "date": date(2023, 3, 9),
        "title": "My lovely Mountains",
        "excerpt": "There's nothing like the view you get when hiking in the mountains. And I wasn't even prepared for what happened whilst I was enjoying the view.",
        "content": """ lorem ipsum dolor sit amet. Fugit nobis pariatur sunt eos quisquam, earum inventore quis ducimus tempora 
                       dolorum cumque aperiam? Fugit tempora facilis. Dolores aliquid eligendi ipsa praesentium quod ab fugiat 
                       minima obcaecati ut. Et quidem hic possimus exercitationem commodi ipsa, id hic quod, dolorum temporibus 
                       
                       dolorem velit cupiditate corporis maxime eum ipsa amet placeat earum, fugit hic adipisci sapiente? Aperiam
                       reiciendis voluptatem mollitia odio quos, voluptate reiciendis voluptatem modi rem corporis in. Iste veritatis 
                       odio vitae animi amet voluptatibus laudantium officia ad deserunt, itaque numquam sint aut accusantium, 
                       exercitationem maiores nihil voluptates, qui facere doloribus harum porro culpa similique repudiandae tenetur 
                       
                       vitae aliquid, fugit error nemo inventore ullam ipsa. Quia rerum repellendus quibusdam quos laborum earum 
                       voluptatem ab, molestiae blanditiis consequatur quis hic dolore at tempora, magni ipsa possimus iure harum, 
                       facilis dolorem iure maiores, eveniet eos porro expedita fuga quae deleniti officiis reprehenderit aspernatur? 
                       Quam labore beatae optio dolore unde nihil a, omnis magnam sequi excepturi atque et repudiandae iure tenetur?"
                       """
    }
]

def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda post: post["date"])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
        })
    
def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    print(identified_post)
    return render(request, "blog/post-detail.html", {
        "post_details": identified_post
    })
