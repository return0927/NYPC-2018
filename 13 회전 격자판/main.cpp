#include "stdafx.h"
#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
	// 인원수, 만남수
	int humans, meets;
	int x, y, c;

	cin >> humans >> meets;

	// 감염자 set
	set<int> influ;

	for (int i = 0; i != meets; i++) {
		cin >> x >> y >> c;
	}


	return 0;
}