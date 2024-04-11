// LoadingScreen.js
import React, { useEffect } from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';

const LoadingScreen = ({ navigation, route }) => {
  useEffect(() => {
    const { companyName, description, motto } = route.params;
    
    // Simulate generating a slogan (you would call your API here)
    setTimeout(() => {
      // Navigate to the slogan display screen after 'loading'
      navigation.navigate('SloganDisplayScreen', { companyName, motto, slogan: "Your Future Starts Here" }); // Example slogan
    }, 2000); // Simulate a 2-second loading time
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Generating your slogan...</Text>
      <ActivityIndicator size="large" color="#0000ff" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    marginBottom: 20,
  },
});

export default LoadingScreen;
