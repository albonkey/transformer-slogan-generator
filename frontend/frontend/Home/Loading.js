// LoadingScreen.js
import React, { useEffect } from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';

const LoadingScreen = ({ navigation, route }) => {
  const { companyName, description } = route.params;
  
  useEffect(() => {
    const fetchSlogan = async () => {
      try {
        
        const response = await fetch('http://192.168.1.27:5000/generate-slogan', {  // Use appropriate IP address
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          
          body: JSON.stringify( {companyName, description} ),
          
        });
        console.log(response.body)
        const json = await response.json();
        if (response.ok) {
          navigation.navigate('Output', { companyName, description, slogan: json.slogan });
        } else {
          console.log('Response Status:', response.status);
          throw new Error(json.error || 'Failed to generate slogan');
        }
      } catch (error) {
        console.error('Fetch Error:', error);
        alert('Failed to generate slogan: ' + error.message);
      }
    };
    

    fetchSlogan();
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
