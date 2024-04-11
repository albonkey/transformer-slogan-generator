// SloganDisplayScreen.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const SloganDisplayScreen = ({ route }) => {
  const { companyName, motto, slogan } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{companyName}</Text>
      <Text style={styles.subtitle}>{motto}</Text>
      <Text style={styles.slogan}>{slogan}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 18,
    fontStyle: 'italic',
    marginBottom: 20,
  },
  slogan: {
    fontSize: 20,
    textAlign: 'center',
  },
});

export default SloganDisplayScreen;
