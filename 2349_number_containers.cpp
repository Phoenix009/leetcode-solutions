class NumberContainers {
private:
    map<int, int> index_number;
    map<int, set<int>> number_index;

public:
    NumberContainers() {
        // No need to re-declare the maps here.
    }
    
    void remove_at(int index) {
        int number = index_number[index];
        number_index[number].erase(index);
        index_number.erase(index);
    }
    
    void add_at(int index, int number) {
        index_number[index] = number;
        number_index[number].insert(index);
    }
    
    void change(int index, int number) {
        if (index_number.count(index)) remove_at(index);
        add_at(index, number);
    }
    
    int find(int number) {
        if (number_index[number].empty()) {
            // Depending on requirements, handle the empty case.
            return -1;
        }
        return *number_index[number].begin();
    }
};

