// HomeScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet, Alert, ActivityIndicator } from 'react-native';

const HomeScreen = ({ navigation }) => {
  const [companyName, setCompanyName] = useState('');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerateSlogan = async () => {
    // Check if the input fields are empty
    if (!companyName.trim() || !description.trim()) {
      Alert.alert("Missing Information", "Please fill in all fields.");
      return;
    }

    setLoading(true);  // Start loading

    // Perform the API request
    try {
      const response = await fetch('http://127.0.0.1:5000/generate-slogan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        
        body: JSON.stringify({ companyName, description }),
        
      });
      

      const json = await response.json();
      if (response.ok) {
        navigation.navigate('SloganDisplayScreen', { companyName, description, slogan: json.slogan });
      } else {
        throw new Error(json.error || 'Failed to generate slogan');
      }
    } catch (error) {
      Alert.alert("Error", `Failed to generate slogan: ${error.message}`);
    } finally {
      setLoading(false);  // Stop loading regardless of outcome
    }
  };

  return (
    <View style={styles.container}>
      {loading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (
        <>
          <TextInput
            placeholder="Company Name"
            value={companyName}
            onChangeText={setCompanyName}
            style={styles.input}
          />
          <TextInput
            placeholder="Description"
            value={description}
            onChangeText={setDescription}
            style={styles.input}
          />
          <Button
            title="Generate Slogan"
            onPress={handleGenerateSlogan}
          />
        </>
      )}
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
  input: {
    width: '100%',
    margin: 10,
    borderBottomWidth: 1,
    borderColor: 'gray',
    padding: 10,
  },
});

export default HomeScreen;
