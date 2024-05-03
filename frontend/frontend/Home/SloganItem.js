import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

const SloganItem = ({ item }) => {
  const [expanded, setExpanded] = useState(false);

  const toggleExpand = () => {
    setExpanded(!expanded);
  };

  // Function to truncate description
  const getTruncatedDescription = (description) => {
    if (description.length > 100 && !expanded) {
      return `${description.substring(0, 100)}...`;
    }
    return description;
  };

  return (
    <TouchableOpacity style={styles.itemContainer} onPress={toggleExpand}>
      <Text style={styles.title}>{item.companyName}</Text>
      <Text style={styles.subtitle}>{item.slogan}</Text>
      <Text style={styles.description}>Description: {getTruncatedDescription(item.description)}</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  itemContainer: {
    backgroundColor: '#f9f9f9',
    padding: 15,
    borderRadius: 8,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginVertical: 4,
  },
  description: {
    fontSize: 14,
  },
});

export default SloganItem;
