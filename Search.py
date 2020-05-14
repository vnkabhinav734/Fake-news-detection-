class Search:
	def main(query):
		query=query+""
		try: 
			from googlesearch import search 
		except ImportError: 
			print("No module named 'google' found") 
		#query = "Bjp news"
		data=list(search(query, tld="co.in", num=10, stop=20))
		print(type(data))
		for j in data:
			print(j)
		return data

if __name__ == '__main__':
	Search.main('bjp modi')

	