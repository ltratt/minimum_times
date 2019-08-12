RUNS?=100000
PYTHON?=python2.7

all: binary_linear_searches.svg binary_search.svg hashmap.svg linear_search.svg

times: binary_search_times hashmap_times linear_search_times

clean:
	rm -f *.svg *.pdf

binary_search_times:
	${PYTHON} run.py binary_search ${RUNS} binary_search_times

hashmap_times:
	${PYTHON} run.py hashmap ${RUNS} hashmap_times

linear_search_times:
	${PYTHON} run.py linear_search ${RUNS} linear_search_times

binary_search.svg: binary_search_times
	rm -f binary_search.pdf binary_search.svg binary_search_pre.svg
	${PYTHON} graph.py binary_search.pdf binary_search_times
	pdftocairo -svg binary_search.pdf binary_search_pre.svg
	scour binary_search_pre.svg binary_search.svg
	rm binary_search_pre.svg

binary_linear_searches.svg: binary_search_times linear_search_times
	rm -f binary_linear_searches.pdf binary_linear_searches.svg binary_linear_searches_pre.svg
	${PYTHON} graph.py binary_linear_searches.pdf binary_search_times linear_search_times
	pdftocairo -svg binary_linear_searches.pdf binary_linear_searches_pre.svg
	scour binary_linear_searches_pre.svg binary_linear_searches.svg
	rm binary_linear_searches_pre.svg

hashmap.svg: hashmap_times
	rm -f hashmap.pdf hashmap.svg hashmap_pre.svg
	${PYTHON} graph.py hashmap.pdf hashmap_times
	pdftocairo -svg hashmap.pdf hashmap_pre.svg
	scour hashmap_pre.svg hashmap.svg
	rm hashmap_pre.svg

linear_search.svg: linear_search_times
	rm -f linear_search.pdf linear_search.svg linear_search_pre.svg
	${PYTHON} graph.py linear_search.pdf linear_search_times
	pdftocairo -svg linear_search.pdf linear_search_pre.svg
	scour linear_search_pre.svg linear_search.svg
	rm linear_search_pre.svg
