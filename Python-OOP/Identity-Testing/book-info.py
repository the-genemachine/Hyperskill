def print_book_info(title, author=None, year=None):
    if author is not None and year is not None:
        print(f"Title: {title}, Author: {author}, Year: {year}")
    elif author is not None:
        print(f"Title: {title}, Author: {author}")
    elif year is not None:
        print(f"Title: {title}, Year: {year}")
    else:
        print(f"Title: {title}")