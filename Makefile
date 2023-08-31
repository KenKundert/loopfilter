all: fig1.svg fig2.svg fig3.svg

fig1.svg: fig1.py
	./fig1.py

fig2.svg: fig2.py
	./fig2.py

fig3.svg: fig3.py
	./fig3.py
