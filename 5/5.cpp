#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <tuple>
#include <regex>
#include <string>
#include <limits>

std::vector<std::tuple<int, int, int>> parseMap(const std::string& mapStr) {
    std::vector<std::tuple<int, int, int>> map;
    std::istringstream iss(mapStr);
    int destStart, srcStart, length;
    while (iss >> destStart >> srcStart >> length) {
        map.emplace_back(destStart, srcStart, length);
    }
    return map;
}

int mapValue(int value, const std::vector<std::tuple<int, int, int>>& mapping) {
    for (const auto& [destStart, srcStart, length] : mapping) {
        if (srcStart <= value && value < srcStart + length) {
            return destStart + (value - srcStart);
        }
    }
    return value;
}

std::vector<int> processMaps(const std::vector<int>& seeds, const std::vector<std::vector<std::tuple<int, int, int>>>& maps) {
    std::vector<int> result = seeds;
    for (const auto& map : maps) {
        for (auto& seed : result) {
            seed = mapValue(seed, map);
        }
    }
    return result;
}

int main() {
    std::ifstream file("5.txt");
    std::string line, input;
    while (getline(file, line)) {
        input += line + "\n";
    }

    std::regex seedsRegex("seeds: ([\\d\\s]+)");
    std::smatch seedsMatch;
    std::regex_search(input, seedsMatch, seedsRegex);
    std::vector<int> seeds;
    std::istringstream seedsStream(seedsMatch[1].str());
    for (int seed; seedsStream >> seed; ) {
        seeds.push_back(seed);
    }

    std::vector<std::vector<std::tuple<int, int, int>>> maps;
    std::regex mapRegex("map:\\n([\\d\\s\\n]+)\\n\\n");
    std::smatch mapMatch;
    while (std::regex_search(input, mapMatch, mapRegex)) {
        maps.push_back(parseMap(mapMatch[1].str()));
        input = mapMatch.suffix().str();
    }

    int lowestLocationNumber = std::numeric_limits<int>::max();
    for (int seed : seeds) {
        int finalValue = seed;
        for (const auto& map : maps) {
            finalValue = mapValue(finalValue, map);
        }
        lowestLocationNumber = std::min(lowestLocationNumber, finalValue);
    }

    std::cout << "Answer 1: " << lowestLocationNumber << std::endl;

    // Part 2 of the problem can be added here following a similar approach.

    return 0;
}
